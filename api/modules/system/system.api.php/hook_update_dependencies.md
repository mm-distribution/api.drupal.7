# hook_update_dependencies()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3571–3589 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3571-L3589)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_update_dependencies()
```

## Documentation

```text
Return an array of information about module update dependencies.

This can be used to indicate update functions from other modules that your
module's update functions depend on, or vice versa. It is used by the update
system to determine the appropriate order in which updates should be run, as
well as to search for missing dependencies.

Implementations of this hook should be placed in a mymodule.install file in
the same directory as mymodule.module.

@return
  A multidimensional array containing information about the module update
  dependencies. The first two levels of keys represent the module and update
  number (respectively) for which information is being returned, and the
  value is an array of information about that update's dependencies. Within
  this array, each key represents a module, and each value represents the
  number of an update function within that module. In the event that your
  update function depends on more than one update from a particular module,
  you should always list the highest numbered one here (since updates within
  a given module always run in numerical order).

@see update_resolve_dependencies()
@see hook_update_N()
```

## Code

```php
function hook_update_dependencies() {
  // Indicate that the mymodule_update_7000() function provided by this module
  // must run after the another_module_update_7002() function provided by the
  // 'another_module' module.
  $dependencies['mymodule'][7000] = array(
    'another_module' => 7002,
  );
  // Indicate that the mymodule_update_7001() function provided by this module
  // must run before the yet_another_module_update_7004() function provided by
  // the 'yet_another_module' module. (Note that declaring dependencies in this
  // direction should be done only in rare situations, since it can lead to the
  // following problem: If a site has already run the yet_another_module
  // module's database updates before it updates its codebase to pick up the
  // newest mymodule code, then the dependency declared here will be ignored.)
  $dependencies['yet_another_module'][7004] = array(
    'mymodule' => 7001,
  );
  return $dependencies;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_update_dependencies()".

- [update_test_1_update_dependencies()](../../simpletest/tests/update_test_1.install/update_test_1_update_dependencies.md) — `modules/simpletest/tests/update_test_1.install`
- [update_test_2_update_dependencies()](../../simpletest/tests/update_test_2.install/update_test_2_update_dependencies.md) — `modules/simpletest/tests/update_test_2.install`
- [update_test_3_update_dependencies()](../../simpletest/tests/update_test_3.install/update_test_3_update_dependencies.md) — `modules/simpletest/tests/update_test_3.install`
- [block_update_dependencies()](../../block/block.install/block_update_dependencies.md) — `modules/block/block.install`
- [comment_update_dependencies()](../../comment/comment.install/comment_update_dependencies.md) — `modules/comment/comment.install`
- [contact_update_dependencies()](../../contact/contact.install/contact_update_dependencies.md) — `modules/contact/contact.install`
- [filter_update_dependencies()](../../filter/filter.install/filter_update_dependencies.md) — `modules/filter/filter.install`
- [forum_update_dependencies()](../../forum/forum.install/forum_update_dependencies.md) — `modules/forum/forum.install`
- [image_update_dependencies()](../../image/image.install/image_update_dependencies.md) — `modules/image/image.install`
- [node_update_dependencies()](../../node/node.install/node_update_dependencies.md) — `modules/node/node.install`
- [system_update_dependencies()](../system.install/system_update_dependencies.md) — `modules/system/system.install`
- [taxonomy_update_dependencies()](../../taxonomy/taxonomy.install/taxonomy_update_dependencies.md) — `modules/taxonomy/taxonomy.install`
- [user_update_dependencies()](../../user/user.install/user_update_dependencies.md) — `modules/user/user.install`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
