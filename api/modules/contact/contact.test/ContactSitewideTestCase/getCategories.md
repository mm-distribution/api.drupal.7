# ContactSitewideTestCase::getCategories()

- **Type:** Method
- **File:** [`modules/contact/contact.test`](../_file.md), lines 292–295 · [local source](../../../../../source/modules/contact/contact.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test#L292-L295)
- **Class:** [ContactSitewideTestCase](../ContactSitewideTestCase.md)
- **Module/theme:** contact

## Signature

```php
function getCategories()
```

## Documentation

```text
Gets a list of all category IDs.

@return array
  A list of the category IDs.
```

## Code

```php
  function getCategories() {
    $categories = db_query('SELECT cid FROM {contact}')->fetchCol();
    return $categories;
  }
```

---
_Drupal 7.103 · [modules/contact/contact.test](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test) · Licensed GPL-2.0-or-later (see LICENSE)._
