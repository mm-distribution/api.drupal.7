# MenuRouterTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/menu.test`](_file.md), lines 124–669 · [local source](../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L124-L669)
- **Module/theme:** batch_test

## Signature

```php
class MenuRouterTestCase extends DrupalWebTestCase
```

## Documentation

_No docblock in source._

## Methods (derived index)

- [getInfo()](MenuRouterTestCase/getInfo.md)
- [setUp()](MenuRouterTestCase/setUp.md)
- [testTitleCallbackFalse()](MenuRouterTestCase/testTitleCallbackFalse.md) — Test title callback set to FALSE.
- [testTitleMenuCallback()](MenuRouterTestCase/testTitleMenuCallback.md) — Tests page title of MENU_CALLBACKs.
- [testThemeCallbackAdministrative()](MenuRouterTestCase/testThemeCallbackAdministrative.md) — Test the theme callback when it is set to use an administrative theme.
- [testThemeCallbackInheritance()](MenuRouterTestCase/testThemeCallbackInheritance.md) — Test that the theme callback is properly inherited.
- [testFileInheritance()](MenuRouterTestCase/testFileInheritance.md) — Test that 'page callback', 'file' and 'file path' keys are properly inherited from parent menu paths.
- [testExoticPath()](MenuRouterTestCase/testExoticPath.md) — Test path containing "exotic" characters.
- [testThemeCallbackMaintenanceMode()](MenuRouterTestCase/testThemeCallbackMaintenanceMode.md) — Test the theme callback when the site is in maintenance mode.
- [testMaintenanceModeLoginPaths()](MenuRouterTestCase/testMaintenanceModeLoginPaths.md) — Make sure the maintenance mode can be bypassed using hook_menu_site_status_alter().
- [testAuthUserUserLogin()](MenuRouterTestCase/testAuthUserUserLogin.md) — Test that an authenticated user hitting 'user/login' gets redirected to 'user' and 'user/register' gets redirected to the user edit page.
- [testThemeCallbackOptionalTheme()](MenuRouterTestCase/testThemeCallbackOptionalTheme.md) — Test the theme callback when it is set to use an optional theme.
- [testThemeCallbackFakeTheme()](MenuRouterTestCase/testThemeCallbackFakeTheme.md) — Test the theme callback when it is set to use a theme that does not exist.
- [testThemeCallbackNoThemeRequested()](MenuRouterTestCase/testThemeCallbackNoThemeRequested.md) — Test the theme callback when no theme is requested.
- [testHookCustomTheme()](MenuRouterTestCase/testHookCustomTheme.md) — Test that hook_custom_theme() can control the theme of a page.
- [testThemeCallbackHookCustomTheme()](MenuRouterTestCase/testThemeCallbackHookCustomTheme.md) — Test that the theme callback wins out over hook_custom_theme().
- [testMenuLinkMaintain()](MenuRouterTestCase/testMenuLinkMaintain.md) — Tests for menu_link_maintain().
- [testMenuGetNames()](MenuRouterTestCase/testMenuGetNames.md) — Test menu_get_names().
- [testMenuName()](MenuRouterTestCase/testMenuName.md) — Tests for menu_name parameter for hook_menu().
- [testMenuHierarchy()](MenuRouterTestCase/testMenuHierarchy.md) — Tests for menu hierarchy.
- [testMenuHidden()](MenuRouterTestCase/testMenuHidden.md) — Tests menu link depth and parents of local tasks and menu callbacks.
- [testMenuGetItemNoAncestors()](MenuRouterTestCase/testMenuGetItemNoAncestors.md) — Test menu_get_item() with empty ancestors.
- [testMenuSetItem()](MenuRouterTestCase/testMenuSetItem.md) — Test menu_set_item().
- [testMenuItemHooks()](MenuRouterTestCase/testMenuItemHooks.md) — Test menu maintenance hooks.
- [testMenuLinkOptions()](MenuRouterTestCase/testMenuLinkOptions.md) — Test menu link 'options' storage and rendering.
- [testMenuItemTitlesCases()](MenuRouterTestCase/testMenuItemTitlesCases.md) — Tests the possible ways to set the title for menu items. Also tests that menu item titles work with string overrides.
- [menuItemTitlesCasesHelper()](MenuRouterTestCase/menuItemTitlesCasesHelper.md) — Get a URL and assert the title given a case number. If override is true, the title is asserted to begin with "Alternative".
- [menuLoadRouter()](MenuRouterTestCase/menuLoadRouter.md) — Load the router for a given path.
- [testMenuLoadArgumentsInheritance()](MenuRouterTestCase/testMenuLoadArgumentsInheritance.md) — Tests inheritance of 'load arguments'.

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
