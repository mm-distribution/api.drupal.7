# forum_form_main()

- **Type:** Function
- **File:** [`modules/forum/forum.admin.inc`](_file.md), lines 22–35 · [local source](../../../../source/modules/forum/forum.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc#L22-L35)
- **Module/theme:** forum

## Signature

```php
function forum_form_main($type, $edit = array())
```

## Documentation

```text
Page callback: Returns a form for creating a new forum or container.

@param $type
  What is being added. Possible values are 'forum' and 'container'.
@param $edit
  (optional) Associative array containing a forum term to be edited.
  Defaults to an empty array.

@return
  A form for creating a new forum or container.

@see forum_menu()
```

## Code

```php
function forum_form_main($type, $edit = array()) {
  $edit = (array) $edit;
  if ((isset($_POST['op']) && $_POST['op'] == t('Delete')) || !empty($_POST['confirm'])) {
    return drupal_get_form('forum_confirm_delete', $edit['tid']);
  }
  switch ($type) {
    case 'forum':
      return drupal_get_form('forum_form_forum', $edit);
      break;
    case 'container':
      return drupal_get_form('forum_form_container', $edit);
      break;
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
