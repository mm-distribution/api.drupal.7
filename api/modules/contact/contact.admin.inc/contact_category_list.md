# contact_category_list()

- **Type:** Function
- **File:** [`modules/contact/contact.admin.inc`](_file.md), lines 11–53 · [local source](../../../../source/modules/contact/contact.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.admin.inc#L11-L53)
- **Module/theme:** contact

## Signature

```php
function contact_category_list()
```

## Documentation

```text
Categories/list tab.
```

## Code

```php
function contact_category_list() {
  $header = array(
    t('Category'),
    t('Recipients'),
    t('Selected'),
    array('data' => t('Operations'), 'colspan' => 2),
  );
  $rows = array();

  // Get all the contact categories from the database.
  $categories = db_select('contact', 'c')
    ->addTag('translatable')
    ->fields('c', array('cid', 'category', 'recipients', 'selected'))
    ->orderBy('weight')
    ->orderBy('category')
    ->execute()
    ->fetchAll();

  // Loop through the categories and add them to the table.
  foreach ($categories as $category) {
    $rows[] = array(
      check_plain($category->category),
      check_plain($category->recipients),
      ($category->selected ? t('Yes') : t('No')),
      l(t('Edit'), 'admin/structure/contact/edit/' . $category->cid),
      l(t('Delete'), 'admin/structure/contact/delete/' . $category->cid),
    );
  }

  if (!$rows) {
    $rows[] = array(array(
      'data' => t('No categories available.'),
      'colspan' => 5,
    ));
  }

  $build['category_table'] = array(
    '#theme' => 'table',
    '#header' => $header,
    '#rows' => $rows,
  );
  return $build;
}
```

---
_Drupal 7.103 · [modules/contact/contact.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
