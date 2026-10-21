# rdf_theme()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 435–444 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L435-L444)
- **Module/theme:** rdf
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function rdf_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function rdf_theme() {
  return array(
    'rdf_template_variable_wrapper' => array(
      'variables' => array('content' => NULL, 'attributes' => array(), 'context' => array(), 'inline' => TRUE),
    ),
    'rdf_metadata' => array(
      'variables' => array('metadata' => array()),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
