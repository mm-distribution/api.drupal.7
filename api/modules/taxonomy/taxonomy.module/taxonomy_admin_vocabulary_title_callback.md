# taxonomy_admin_vocabulary_title_callback()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 388–390 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L388-L390)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_admin_vocabulary_title_callback($vocabulary)
```

## Documentation

```text
Returns the sanitized name of a vocabulary.

Deprecated. This function was previously used as a menu item title callback
but has been replaced by using entity_label() (which does not
sanitize the title, since the menu system does that automatically). In
Drupal 7, use that function for title callbacks, and call check_plain()
directly if you need a sanitized title.
```

## Code

```php
function taxonomy_admin_vocabulary_title_callback($vocabulary) {
  return check_plain($vocabulary->name);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
