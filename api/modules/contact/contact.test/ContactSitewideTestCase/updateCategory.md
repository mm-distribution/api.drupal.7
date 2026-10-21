# ContactSitewideTestCase::updateCategory()

- **Type:** Method
- **File:** [`modules/contact/contact.test`](../_file.md), lines 239–248 · [local source](../../../../../source/modules/contact/contact.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test#L239-L248)
- **Class:** [ContactSitewideTestCase](../ContactSitewideTestCase.md)
- **Module/theme:** contact

## Signature

```php
function updateCategory($categories, $category, $recipients, $reply, $selected)
```

## Documentation

```text
Updates a category.

@param string $category
  The category name.
@param string $recipients
  The list of recipient e-mail addresses.
@param string $reply
  The auto-reply text that is sent to a user upon completing the contact
  form.
@param boolean $selected
  Boolean indicating whether the category should be selected by default.
```

## Code

```php
  function updateCategory($categories, $category, $recipients, $reply, $selected) {
    $category_id = $categories[array_rand($categories)];
    $edit = array();
    $edit['category'] = $category;
    $edit['recipients'] = $recipients;
    $edit['reply'] = $reply;
    $edit['selected'] = ($selected ? '1' : '0');
    $this->drupalPost('admin/structure/contact/edit/' . $category_id, $edit, t('Save'));
    return ($category_id);
  }
```

---
_Drupal 7.103 · [modules/contact/contact.test](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test) · Licensed GPL-2.0-or-later (see LICENSE)._
