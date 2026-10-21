# ContactSitewideTestCase::deleteCategories()

- **Type:** Method
- **File:** [`modules/contact/contact.test`](../_file.md), lines 277–284 · [local source](../../../../../source/modules/contact/contact.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test#L277-L284)
- **Class:** [ContactSitewideTestCase](../ContactSitewideTestCase.md)
- **Module/theme:** contact

## Signature

```php
function deleteCategories()
```

## Documentation

```text
Deletes all categories.
```

## Code

```php
  function deleteCategories() {
    $categories = $this->getCategories();
    foreach ($categories as $category) {
      $category_name = db_query("SELECT category FROM {contact} WHERE cid = :cid", array(':cid' => $category))->fetchField();
      $this->drupalPost('admin/structure/contact/delete/' . $category, array(), t('Delete'));
      $this->assertRaw(t('Category %category has been deleted.', array('%category' => $category_name)), 'Category deleted successfully.');
    }
  }
```

---
_Drupal 7.103 · [modules/contact/contact.test](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test) · Licensed GPL-2.0-or-later (see LICENSE)._
