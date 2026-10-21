# shortcut_set_admin()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 169–191 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L169-L191)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_admin()
```

## Documentation

```text
Menu page callback: builds the page for administering shortcut sets.
```

## Code

```php
function shortcut_set_admin() {
  $shortcut_sets = shortcut_sets();
  $header = array(t('Name'), array('data' => t('Operations'), 'colspan' => 4));

  $rows = array();
  foreach ($shortcut_sets as $set) {
    $row = array(
      check_plain($set->title),
      l(t('list links'), "admin/config/user-interface/shortcut/$set->set_name"),
      l(t('edit set name'), "admin/config/user-interface/shortcut/$set->set_name/edit"),
    );
    if (shortcut_set_delete_access($set)) {
      $row[] = l(t('delete set'), "admin/config/user-interface/shortcut/$set->set_name/delete");
    }
    else {
      $row[] = '';
    }

    $rows[] = $row;
  }

  return theme('table', array('header' => $header, 'rows' => $rows));
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
