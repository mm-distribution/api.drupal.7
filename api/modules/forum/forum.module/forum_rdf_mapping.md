# forum_rdf_mapping()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 1376–1397 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L1376-L1397)
- **Module/theme:** forum
- **Implements:** [hook_rdf_mapping()](../../rdf/rdf.api.php/hook_rdf_mapping.md)

## Signature

```php
function forum_rdf_mapping()
```

## Documentation

```text
Implements hook_rdf_mapping().
```

## Code

```php
function forum_rdf_mapping() {
  return array(
    array(
      'type' => 'node',
      'bundle' => 'forum',
      'mapping' => array(
        'rdftype' => array('sioc:Post', 'sioct:BoardPost'),
        'taxonomy_forums' => array(
          'predicates' => array('sioc:has_container'),
          'type' => 'rel',
        ),
      ),
    ),
    array(
      'type' => 'taxonomy_term',
      'bundle' => 'forums',
      'mapping' => array(
        'rdftype' => array('sioc:Container', 'sioc:Forum'),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
