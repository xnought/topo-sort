from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    data: str
    children: list[Node] | None = None


def topo_sort(start: Node) -> list[Node]:
    result = []

    def _dfs(d: Node):
        nonlocal result  # points to result in topo_sort scope
        if d.children is None:
            # no other dependencies, so can add to result
            result.append(d)
            return

        for c in d.children:
            _dfs(c)
        # once we visit all the children in a given node, add it to the result
        result.append(d)

    _dfs(start)
    return result


def main():
    #      f
    #      \
    # a -> c -> d
    # b |
    a = Node("a")
    f = Node("f")
    b = Node("b")
    c = Node("c", children=[a, b, f])
    d = Node("d", children=[c])

    print(list(map(lambda x: x.data, topo_sort(d))))


if __name__ == "__main__":
    main()
