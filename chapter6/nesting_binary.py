test_list = [
    [(1.0, 2.5), (3.5, 4.0), (2.5, 1.5)],
    [(7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0)],
    [(3.4, 6.3), (1.2, 0.5), (4.6, 9.2)],
]

import struct
import itertools

def write_polys(file_name, polys):
    # Determine bounding box
    flattened = list(itertools.chain(*polys))
    min_x = min(x for x, y in flattened)
    max_x = max(x for x, y in flattened)
    min_y = min(y for x, y in flattened)
    max_y = max(y for x, y in flattened)
    with open(file_name, 'wb') as f:
        f.write(struct.pack('<iddddi', 0x1234,
                            min_x, min_y,
                            max_x, max_y,
                            len(polys)))
        for poly in polys:
            size = len(poly) * struct.calcsize('<dd')
            f.write(struct.pack('<i', size + 4))
            for pt in poly:
                f.write(struct.pack('<dd', *pt))

if __name__ == '__main__':
    write_polys('test.bin', test_list)


def read_polys(file_name):
    with open(file_name, 'rb') as f:
        # Read the header
        header = f.read(40)
        file_code, min_x, min_y, max_x, max_y, num_polys = \
            struct.unpack('<iddddi', header)
        polys = []
        for n in range(num_polys):
            pbytes, = struct.unpack('<i', f.read(4))
            poly = []
            for m in range(pbytes // 16):
                pt = struct.unpack('<dd', f.read(16))
                poly.append(pt)
            polys.append(poly)
    return polys


import struct

class StructField:
    """
    Descriptor representing a simple structure field
    """
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r

class Structure:
    def __init__(self, byte_data):
        self._buffer = memoryview(byte_data)


class PolyHeader(Structure):
    file_code = StructField('<i', 0)
    min_x = StructField('<d', 4)
    min_y = StructField('<d', 12)
    max_x = StructField('<d', 20)
    max_y = StructField('<d', 28)
    num_polys = StructField('<i', 36)


f = open('test.bin', 'rb')
phead = PolyHeader(f.read(40))
print(f'file code is: {phead.file_code == 0x1234}')
print(f'min x is: {phead.min_x}')
print(f'min y is: {phead.min_y}')
print(f'max x is: {phead.max_x}')
print(f'max y is: {phead.max_y}')
print(f'num polys is: {phead.num_polys}')


class StructureMeta(type):
    """
    Metaclass that automatically creates StructField descriptors
    """
    def __init__(self, cls_name, bases, cls_dict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, field_name in fields:
            if format.startswith(('<','>','!','@')):
                byte_order = format[0]
                format = format[1:]
            format = byte_order + format
            setattr(self, field_name, StructField(format, offset))
            offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)

class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        ('d', 'min_x'),
        ('d', 'min_y'),
        ('d', 'max_x'),
        ('d', 'max_y'),
        ('i', 'num_polys')
    ]


f = open('test.bin', 'rb')
phead = PolyHeader.from_file(f)
print(f'file code is: {phead.file_code == 0x1234}')
print(f'min x is: {phead.min_x}')
print(f'min y is: {phead.min_y}')
print(f'max x is: {phead.max_x}')
print(f'max y is: {phead.max_y}')
print(f'num polys is: {phead.num_polys}')


class NestedStruct:
    """
    Descriptor representing a nested structure
    """
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[self.offset:
                            self.offset+self.struct_type.struct_size]
            result = self.struct_type(data)
            setattr(instance, self.name, result)
            return result

class StructureMeta(type):
    """
    Metaclass that automatically creates StructField descriptors
    """
    def __init__(self, cls_name, bases, cls_dict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, field_name in fields:
            if isinstance(format, StructureMeta):
                setattr(self, field_name,
                        NestedStruct(field_name, format, offset))
                offset += format.struct_size
            else:
                if format.startswith(('<','>','!','@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, field_name, StructField(format, offset))
                offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class Point(Structure):
    _fields_ = [
        ('<d', 'x'),
        ('d', 'y')
    ]

class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        (Point, 'min'), # nested struct
        (Point, 'max'), # nested struct
        ('i', 'num_polys')
    ]


f = open('test.bin', 'rb')
phead = PolyHeader.from_file(f)
print(f'file code is: {phead.file_code == 0x1234}')
print(f'min is: {phead.min}')
print(f'min x is: {phead.min_x}')
print(f'min y is: {phead.min_y}')
print(f'max x is: {phead.max_x}')
print(f'max y is: {phead.max_y}')
print(f'num polys is: {phead.num_polys}')


class SizedRecord:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

    @classmethod
    def from_file(cls, f, size_fmt, includes_size=True):
        sz_nbytes = struct.calcsize(size_fmt)
        sz_bytes = f.read(sz_nbytes)
        sz, = struct.unpack(size_fmt, sz_bytes)
        buf = f.read(sz - includes_size * sz_nbytes)
        return cls(buf)

    def iter_as(self, code):
        if isinstance(code, str):
            s = struct.Struct(code)
            for off in range(0, len(self._buffer), s.size):
                yield s.unpack_from(self._buffer, off)
        elif isinstance(code, StructureMeta):
            size = code.struct_size
            for off in range(0, len(self._buffer), size):
                data = self._buffer[off:off+size]
                yield code(data)


f = open('test.bin', 'rb')
phead = PolyHeader.from_file(f)
print(f'num polys is: {phead.num_polys}')
polydata = [ SizedRecord.from_file(f, '<i') for n in range(phead.num_polys) ]
print(f'poly data: {polydata}')


for n, poly in enumerate(polydata):
    print(f'Polygon {n}')
    for p in poly.iter_as('<dd'):
        print(f'poly iter: {p}')

for n, poly in enumerate(polydata):
    print(f'Polygon {n}')
    for p in poly.iter_as(Point):
        print(f'p.x = {p.x}, p.y = {p.y}')


class Point(Structure):
    _fields_ = [
        ('<d', 'x'),
        ('d', 'y')
    ]

class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        (Point, 'min'),
        (Point, 'max'),
        ('i', 'num_polys')
    ]

def read_polys(file_name):
    polys = []
    with open(file_name, 'rb') as f:
        phead = PolyHeader.from_file(f)
        for n in range(phead.num_polys):
            rec = SizedRecord.from_file(f, '<i')
            poly = [ (p.x, p.y) for p in rec.iter_as(Point) ]
            polys.append(poly)
    return polys


class ShapeFile(Structure):
    _fields_ = [('>i', 'file_code'), # Big endian
        ('20s', 'unused'),
        ('i', 'file_length'),
        ('<i', 'version'), # Little endian
        ('i', 'shape_type'),
        ('d', 'min_x'),
        ('d', 'min_y'),
        ('d', 'max_x'),
        ('d', 'max_y'),
        ('d', 'min_z'),
        ('d', 'max_z'),
        ('d', 'min_m'),
        ('d', 'max_m')]
