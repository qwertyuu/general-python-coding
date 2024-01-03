# ur-2d6-optimal

Le problème est sorti en janvier 2024 sur le discord de ur ou quelqu'un essaie de trouver la façon optimale de réarranger deux d6 comme un ensemble de 4 dés binaires de ur.

J'ai donc pensé à une façon de le faire, en énumérant chaque possibilité de réarranger les 2x6 faces des d6 avec des valeurs de 0 à 2 et en calculant les possibilités de lancers puis en calculant la probabilité finale. Le tout permettant de calculer la différence avec la proportion "target", soit celle de Ur originale de 4d2. Puis, finalement, je trouve la configuration avec le moins de différence et le tour est joué!