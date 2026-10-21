# taxonomy_term_show()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 760–762 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L760-L762)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_term_show($term)
```

## Documentation

```text
Generates an array which displays a term detail page.

@param term
  A taxonomy term object.
@return
  A $page element suitable for use by drupal_render().
```

## Code

```php
function taxonomy_term_show($term) {
  return taxonomy_term_view_multiple(array($term->tid => $term), 'full');
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
