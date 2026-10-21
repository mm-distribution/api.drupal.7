# book_admin_edit()

- **Type:** Function
- **File:** [`modules/book/book.admin.inc`](_file.md), lines 83–93 · [local source](../../../../source/modules/book/book.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc#L83-L93)
- **Module/theme:** book
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function book_admin_edit($form, $form_state, $node)
```

## Documentation

```text
Form constructor for administering a single book's hierarchy.

@see book_admin_edit_submit()

@param $node
  The node of the top-level page in the book.

@see book_admin_edit_validate()
@see book_admin_edit_submit()
@ingroup forms
```

## Code

```php
function book_admin_edit($form, $form_state, $node) {
  drupal_set_title($node->title);
  $form['#node'] = $node;
  _book_admin_table($node, $form);
  $form['save'] = array(
    '#type' => 'submit',
    '#value' => t('Save book pages'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/book/book.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
