# taxonomy_term_title()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1729–1731 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1729-L1731)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_term_title($term)
```

## Documentation

```text
Title callback: Returns the title of the taxonomy term.

@param $term
  A term object.

@return
  An unsanitized string that is the title of the taxonomy term.

@see taxonomy_menu()
```

## Code

```php
function taxonomy_term_title($term) {
  return $term->name;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
