# contact_load()

- **Type:** Function
- **File:** [`modules/contact/contact.module`](_file.md), lines 156–163 · [local source](../../../../source/modules/contact/contact.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module#L156-L163)
- **Module/theme:** contact

## Signature

```php
function contact_load($cid)
```

## Documentation

```text
Loads a contact category.

@param $cid
  The contact category ID.

@return
  An array with the contact category's data.
```

## Code

```php
function contact_load($cid) {
  return db_select('contact', 'c')
    ->addTag('translatable')
    ->fields('c')
    ->condition('cid', $cid)
    ->execute()
    ->fetchAssoc();
}
```

---
_Drupal 7.103 · [modules/contact/contact.module](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module) · Licensed GPL-2.0-or-later (see LICENSE)._
