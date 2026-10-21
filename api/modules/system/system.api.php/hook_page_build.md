# hook_page_build()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 905–914 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L905-L914)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_page_build(&$page)
```

## Documentation

```text
Add elements to a page before it is rendered.

Use this hook when you want to add elements at the page level. For your
additions to be printed, they have to be placed below a top level array key
of the $page array that has the name of a region of the active theme.

By default, valid region keys are 'page_top', 'header', 'sidebar_first',
'content', 'sidebar_second' and 'page_bottom'. To get a list of all regions
of the active theme, use system_region_list($theme). Note that $theme is a
global variable.

If you want to alter the elements added by other modules or if your module
depends on the elements of other modules, use hook_page_alter() instead which
runs after this hook.

@param $page
  Nested array of renderable elements that make up the page.

@see hook_page_alter()
@see drupal_render_page()
```

## Code

```php
function hook_page_build(&$page) {
  if (menu_get_object('node', 1)) {
    // We are on a node detail page. Append a standard disclaimer to the
    // content region.
    $page['content']['disclaimer'] = array(
      '#markup' => t('Acme, Inc. is not responsible for the contents of this sample code.'),
      '#weight' => 25,
    );
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_page_build()".

- [system_test_page_build()](../../simpletest/tests/system_test.module/system_test_page_build.md) — `modules/simpletest/tests/system_test.module`
- [block_page_build()](../../block/block.module/block_page_build.md) — `modules/block/block.module`
- [dashboard_page_build()](../../dashboard/dashboard.module/dashboard_page_build.md) — `modules/dashboard/dashboard.module`
- [toolbar_page_build()](../../toolbar/toolbar.module/toolbar_page_build.md) — `modules/toolbar/toolbar.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
