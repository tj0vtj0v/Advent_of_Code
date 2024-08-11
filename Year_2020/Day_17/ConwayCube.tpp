//
// Created by Tjorven on 11.08.2024.
//

#include "ConwayCube.h"

ConwayCube::ConwayCube() = default;

Haufen<Cube> ConwayCube::createHaufen() {
    auto haufen = Haufen<Cube>();

    for (auto cell: this->active) {
        for (int x = -1; x <= 1; x++) {
            for (int y = -1; y <= 1; y++) {
                for (int z = -1; z <= 1; z++) {
                    auto toAdd = Cube({cell.getX() + x, cell.getY() + y, cell.getZ() + z});
                    if (x != 0 || y != 0 || z != 0) {
                        haufen.addElement(toAdd);
                    }
                }
            }
        }
    }

    return haufen;
}