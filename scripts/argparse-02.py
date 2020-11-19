import argparse


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('interface', type=str,
                   help='Name of the interface we want to route through')
parser.add_argument('-add', action='store_true', help='Add routes to amazon VMs')
parser.add_argument('-del', action='store_true', help='Delete routes to amazon VMs')

args = parser.parse_args()
import pdb;pdb.set_trace()
print(args.accumulate(args.integers))


if __name__ == "__main__":
    main()

# -> print(args.accumulate(args.integers))
# (Pdb++) args
# Namespace(add=True, del=True, interface='asd')
# (Pdb++) args.add
# True
# (Pdb++) args.interface
# 'asd'
# (Pdb++)

