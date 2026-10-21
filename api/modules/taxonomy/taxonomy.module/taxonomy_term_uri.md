# taxonomy_term_uri()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 145–149 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L145-L149)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_term_uri($term)
```

## Documentation

```text
Implements callback_entity_info_uri().
```

## Code

```php
function taxonomy_term_uri($term) {
  return array(
    'path' => 'taxonomy/term/' . $term->tid,
  );
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
