# taxonomy_update_7007()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 841–843 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L841-L843)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_update_7007()
```

## Documentation

```text
Add index on {taxonomy_term_data}.name column to speed up taxonomy_get_term_by_name().
```

## Code

```php
function taxonomy_update_7007() {
  db_add_index('taxonomy_term_data', 'name', array('name'));
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
