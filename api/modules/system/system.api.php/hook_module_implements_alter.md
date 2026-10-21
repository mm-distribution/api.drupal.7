# hook_module_implements_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2022–2032 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2022-L2032)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_module_implements_alter(&$implementations, $hook)
```

## Documentation

```text
Alter the registry of modules implementing a hook.

This hook is invoked during module_implements(). A module may implement this
hook in order to reorder the implementing modules, which are otherwise
ordered by the module's system weight.

Note that hooks invoked using drupal_alter() can have multiple variations
(such as hook_form_alter() and hook_form_FORM_ID_alter()). drupal_alter()
will call all such variants defined by a single module in turn. For the
purposes of hook_module_implements_alter(), these variants are treated as
a single hook. Thus, to ensure that your implementation of
hook_form_FORM_ID_alter() is called at the right time, you will have to
change the order of hook_form_alter() implementation in
hook_module_implements_alter().

@param $implementations
  An array keyed by the module's name. The value of each item corresponds
  to a $group, which is usually FALSE, unless the implementation is in a
  file named $module.$group.inc.
@param $hook
  The name of the module hook being implemented.
```

## Code

```php
function hook_module_implements_alter(&$implementations, $hook) {
  if ($hook == 'rdf_mapping') {
    // Move my_module_rdf_mapping() to the end of the list. module_implements()
    // iterates through $implementations with a foreach loop which PHP iterates
    // in the order that the items were added, so to move an item to the end of
    // the array, we remove it and then add it.
    $group = $implementations['my_module'];
    unset($implementations['my_module']);
    $implementations['my_module'] = $group;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_module_implements_alter()".

- [common_test_module_implements_alter()](../../simpletest/tests/common_test.module/common_test_module_implements_alter.md) — `modules/simpletest/tests/common_test.module`
- [module_test_module_implements_alter()](../../simpletest/tests/module_test.module/module_test_module_implements_alter.md) — `modules/simpletest/tests/module_test.module`
- [system_test_module_implements_alter()](../../simpletest/tests/system_test.module/system_test_module_implements_alter.md) — `modules/simpletest/tests/system_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
