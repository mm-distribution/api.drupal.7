# taxonomy_term_is_page()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 950–953 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L950-L953)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_term_is_page($term)
```

## Documentation

```text
Returns whether the current page is the page of the passed-in term.

@param $term
  A term object.
```

## Code

```php
function taxonomy_term_is_page($term) {
  $page_term = menu_get_object('taxonomy_term', 2);
  return (!empty($page_term) ? $page_term->tid == $term->tid : FALSE);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
