"""
Post type

Applies type information to parsed types which possibly do not contain
such info in their actual source code.

"""
from mypy.types import Callable, UnboundType
from mypy.nodes import ARG_POS, ARG_OPT, ARG_STAR, ARG_NAMED, ARG_STAR2

INT_TYPE = UnboundType('int')
STR_TYPE = UnboundType('str')


def Func(types=(), ret=None):
    """Constructs a Callable but makes sure the arrays are all synced up."""
    return Callable(arg_types=[element[0] for element in types],
                    arg_kinds=[element[1] for element in types],
                    arg_names=[element[2] for element in types],
                    ret_type=ret,
                    is_type_obj=False)


funcs = {
    "do_something": Func([(STR_TYPE, ARG_POS, "a")], ret=INT_TYPE),
    "function_a": Func([], ret=INT_TYPE),
    "i_am_a_cow": Func([], ret=STR_TYPE),
}


def debug_print(msg):
    #print(msg)
    pass


class FuncBuilder():

    def __init__(self, *args, **kwargs):
        self.__dict__.update(**kwargs)
        self.typ = funcs.get(self.name, self.typ)
        debug_print("\t%s = (args, init, kinds, typ, arg_repr)" % self.name)
        debug_print("\t%s = (%s, %s, %s, %s, %s)" % (self.name, self.args, self.init,
                    self.kinds, self.typ, self.arg_repr))
        debug_print("%s type of type=%s" % (self.name, type(self.typ)))

    def get(self):
        return (self.name, self.args, self.init, self.kinds, self.typ,
                self.arg_repr)


def mod_func(name, args, init, kinds, typ, arg_repr):
    fb = FuncBuilder(name=name, args=args, init=init, kinds=kinds, typ=typ,
                     arg_repr=arg_repr)
    return fb.get()


