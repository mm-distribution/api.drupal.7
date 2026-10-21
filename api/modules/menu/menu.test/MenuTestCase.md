# MenuTestCase

- **Type:** Class
- **File:** [`modules/menu/menu.test`](_file.md), lines 8–724 · [local source](../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L8-L724)
- **Module/theme:** menu

## Signature

```php
class MenuTestCase extends DrupalWebTestCase
```

## Documentation

_No docblock in source._

## Properties

### $big_user

```php
protected $big_user;
```

### $std_user

```php
protected $std_user;
```

### $menu

```php
protected $menu;
```

### $items

```php
protected $items;
```

## Methods (derived index)

- [getInfo()](MenuTestCase/getInfo.md)
- [setUp()](MenuTestCase/setUp.md)
- [testMenu()](MenuTestCase/testMenu.md) — Login users, add menus and menu links, and test menu functionality through the admin and user interfaces.
- [doStandardMenuTests()](MenuTestCase/doStandardMenuTests.md) — Test standard menu functionality using navigation menu.
- [doCustomMenuTests()](MenuTestCase/doCustomMenuTests.md) — Test custom menu functionality using navigation menu.
- [addCustomMenuCRUD()](MenuTestCase/addCustomMenuCRUD.md) — Add custom menu using CRUD functions.
- [addCustomMenu()](MenuTestCase/addCustomMenu.md) — Add custom menu.
- [deleteCustomMenu()](MenuTestCase/deleteCustomMenu.md) — Delete custom menu.
- [doMenuTests()](MenuTestCase/doMenuTests.md) — Test menu functionality using navigation menu.
- [testMenuQueryAndFragment()](MenuTestCase/testMenuQueryAndFragment.md) — Add and remove a menu link with a query string and fragment.
- [testNavigationAsSecondaryMenu()](MenuTestCase/testNavigationAsSecondaryMenu.md) — Tries to use the navigation menu as the source for secondary links.
- [addMenuLink()](MenuTestCase/addMenuLink.md) — Add a menu link using the menu module UI.
- [addInvalidMenuLink()](MenuTestCase/addInvalidMenuLink.md) — Attempt to add menu link with invalid path or no access permission.
- [verifyMenuLink()](MenuTestCase/verifyMenuLink.md) — Verify a menu link using the menu module UI.
- [moveMenuLink()](MenuTestCase/moveMenuLink.md) — Change the parent of a menu link using the menu module UI.
- [modifyMenuLink()](MenuTestCase/modifyMenuLink.md) — Modify a menu link using the menu module UI.
- [resetMenuLink()](MenuTestCase/resetMenuLink.md) — Reset a standard menu link using the menu module UI.
- [deleteMenuLink()](MenuTestCase/deleteMenuLink.md) — Delete a menu link using the menu module UI.
- [toggleMenuLink()](MenuTestCase/toggleMenuLink.md) — Alternately disable and enable a menu link.
- [disableMenuLink()](MenuTestCase/disableMenuLink.md) — Disable a menu link.
- [enableMenuLink()](MenuTestCase/enableMenuLink.md) — Enable a menu link.
- [assertMenuLink()](MenuTestCase/assertMenuLink.md) — Fetch the menu item from the database and compare it to the specified array.
- [testMenuParentsJsAccess()](MenuTestCase/testMenuParentsJsAccess.md) — Test administrative users other than user 1 can access the menu parents AJAX callback.
- [getStandardMenuLink()](MenuTestCase/getStandardMenuLink.md) — Get standard menu link.
- [verifyAccess()](MenuTestCase/verifyAccess.md) — Verify the logged in user has the desired access to the various menu nodes.
- [testUnpublishedNodeMenuItem()](MenuTestCase/testUnpublishedNodeMenuItem.md) — Tests that menu admin lists can include menu items for unpublished nodes.
- [assertNoOption()](MenuTestCase/assertNoOption.md) — Asserts that a select option in the current page does not exist.
- [assertOption()](MenuTestCase/assertOption.md) — Asserts that a select option in the current page exist.

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
