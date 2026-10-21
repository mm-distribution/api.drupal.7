# MenuTestCase::addInvalidMenuLink()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 362–371 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L362-L371)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function addInvalidMenuLink($menu_name = 'navigation')
```

## Documentation

```text
Attempt to add menu link with invalid path or no access permission.

@param string $menu_name Menu name.
```

## Code

```php
  function addInvalidMenuLink($menu_name = 'navigation') {
    foreach (array('-&-', 'admin/people/permissions', '#') as $link_path) {
      $edit = array(
        'link_path' => $link_path,
        'link_title' => 'title',
      );
      $this->drupalPost("admin/structure/menu/manage/$menu_name/add", $edit, t('Save'));
      $this->assertRaw(t("The path '@path' is either invalid or you do not have access to it.", array('@path' => $link_path)), 'Menu link was not created');
    }
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
