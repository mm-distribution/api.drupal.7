# poll_rdf_mapping()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 1001–1011 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L1001-L1011)
- **Module/theme:** poll
- **Implements:** [hook_rdf_mapping()](../../rdf/rdf.api.php/hook_rdf_mapping.md)

## Signature

```php
function poll_rdf_mapping()
```

## Documentation

```text
Implements hook_rdf_mapping().
```

## Code

```php
function poll_rdf_mapping() {
  return array(
    array(
      'type' => 'node',
      'bundle' => 'poll',
      'mapping' => array(
        'rdftype' => array('sioc:Post', 'sioct:Poll'),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
