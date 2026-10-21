# book_remove_form()

- **Type:** Function
- **File:** [`modules/book/book.pages.inc`](_file.md), lines 220–232 · [local source](../../../../source/modules/book/book.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc#L220-L232)
- **Module/theme:** book
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function book_remove_form($form, &$form_state, $node)
```

## Documentation

```text
Form constructor to confirm removal of a node from a book.

@param $node
  The node to delete.

@see book_remove_form_submit()
@ingroup forms
```

## Code

```php
function book_remove_form($form, &$form_state, $node) {
  $form['#node'] = $node;
  $title = array('%title' => $node->title);

  if ($node->book['has_children']) {
    $description = t('%title has associated child pages, which will be relocated automatically to maintain their connection to the book. To recreate the hierarchy (as it was before removing this page), %title may be added again using the Outline tab, and each of its former child pages will need to be relocated manually.', $title);
  }
  else {
    $description = t('%title may be added to hierarchy again using the Outline tab.', $title);
  }

  return confirm_form($form, t('Are you sure you want to remove %title from the book hierarchy?', $title), 'node/' . $node->nid, $description, t('Remove'));
}
```

---
_Drupal 7.103 · [modules/book/book.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
