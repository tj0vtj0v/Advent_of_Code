//
// Created by Tjorven on 11.08.2024.
//

#include "ConwayHyperCube.h"

ConwayHyperCube::ConwayHyperCube() = default;

Haufen<HyperCube> ConwayHyperCube::createHaufen() {
    auto haufen = Haufen<HyperCube>();

    for (auto cell: this->active) {
        for (int x = -1; x <= 1; x++) {
            for (int y = -1; y <= 1; y++) {
                for (int z = -1; z <= 1; z++) {
                    for (int w = -1; w <= 1; w++) {
                        auto toAdd = HyperCube({cell.getX() + x, cell.getY() + y, cell.getZ() + z, cell.getW() + w});
                        if (x != 0 || y != 0 || z != 0 || w != 0) {
                            haufen.addElement(toAdd);
                        }
                    }
                }
            }
        }
    }

    return haufen;
}
