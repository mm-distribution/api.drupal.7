# shortcut_install()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.install`](_file.md), lines 11–36 · [local source](../../../../source/modules/shortcut/shortcut.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.install#L11-L36)
- **Module/theme:** shortcut
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function shortcut_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function shortcut_install() {
  $t = get_t();
  // Create an initial default shortcut set.
  $shortcut_set = new stdClass();
  $shortcut_set->title = $t('Default');
  $shortcut_set->links = array(
    array(
      'link_path' => 'node/add',
      'link_title' => $t('Add content'),
      'weight' => -20,
    ),
    array(
      'link_path' => 'admin/content',
      'link_title' => $t('Find content'),
      'weight' => -19,
    ),
  );
  // If Drupal is being installed, rebuild the menu before saving the shortcut
  // set, to make sure the links defined above can be correctly saved. (During
  // installation, the menu might not have been built at all yet, or it might
  // have been built but without the node module's links in it.)
  if (drupal_installation_attempted()) {
    menu_rebuild();
  }
  shortcut_set_save($shortcut_set);
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.install](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.install) · Licensed GPL-2.0-or-later (see LICENSE)._
