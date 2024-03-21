# Modélisation UML - Paris Sportif

## Description
Ce projet présente une modélisation UML détaillée pour un système de gestion de projets. Il inclut des diagrammes pour illustrer les interactions entre les acteurs, les cas d'utilisation, les séquences d'événements et les états des objets. De plus, il présente un prototype développé avec OpenXava pour démontrer la mise en œuvre de la modélisation.

## Table des Matières
- [Les acteurs](#les-acteurs)
- [Le diagramme de cas d'utilisation](#le-diagramme-de-cas-dutilisation)
- [Le diagramme de casses](#le-diagramme-de-classes)
- [Le diagramme de séquence](#le-diagramme-de-séquence)
- [Le diagramme d'etat](#le-diagramme-détat)
- [Prototype avec OpenXava](#prototype-avec-openxava)
- [Démonstration du Prototype](#démonstration-du-prototype)

## Les Acteurs
Notre système comprend deux acteurs principaux : le parieur et le bookmaker, ainsi qu'un acteur secondaire, le "système tiers". Cependant, dans la suite de notre diagramme de cas d'utilisation, nous avons mis l'accent sur les acteurs principaux.

## Le Diagramme de Cas d'Utilisation

![Diagramme de cas d'utilisation](diagrams/usecase.png)

## Le diagramme de classes
Notre diagramme de classe comprend un total de 9 classes, dont deux (pari simple et pari avancé) qui héritent de la classe parente "pari".

![Diagramme d'État](diagrams/class.png)

## Le Diagramme de Séquence
Nous avons modélisé deux diagrammes de séquence en nous assurant de gérer tous les cas alternatifs possibles.

### Placer un pari
![Diagramme d'État](diagrams/state_pari.png)

### Configurer un evenement
![Diagramme d'État](diagrams/state_event.png)


## Le Diagramme d'État

### Paris
![Diagramme d'État](diagrams/state_pari.png)

### Evenements
![Diagramme d'État](diagrams/state_event.png)

## Prototype avec OpenXava
OpenXava est utilisé pour développer rapidement des applications web. Il fournit un cadre pour la modélisation des données et la génération de l'interface utilisateur.

## Démonstration du Prototype
La démonstration du prototype illustre comment les utilisateurs interagissent avec le système. Elle peut inclure des captures d'écran ou des vidéos montrant les fonctionnalités clés du système.
