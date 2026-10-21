# taxonomy_theme()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 241–254 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L241-L254)
- **Module/theme:** taxonomy
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function taxonomy_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function taxonomy_theme() {
  return array(
    'taxonomy_overview_vocabularies' => array(
      'render element' => 'form',
    ),
    'taxonomy_overview_terms' => array(
      'render element' => 'form',
    ),
    'taxonomy_term' => array(
      'render element' => 'elements',
      'template' => 'taxonomy-term',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
