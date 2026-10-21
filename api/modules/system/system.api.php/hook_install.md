# hook_install()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3400–3412 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3400-L3412)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_install()
```

## Documentation

```text
Perform setup tasks when the module is installed.

If the module implements hook_schema(), the database tables will
be created before this hook is fired.

Implementations of this hook are by convention declared in the module's
.install file. The implementation can rely on the .module file being loaded.
The hook will only be called the first time a module is enabled or after it
is re-enabled after being uninstalled. The module's schema version will be
set to the module's greatest numbered update hook. Because of this, any time
a hook_update_N() is added to the module, this function needs to be updated
to reflect the current version of the database schema.

See the @link http://drupal.org/node/146843 Schema API documentation @endlink
for details on hook_schema and how database tables are defined.

Note that since this function is called from a full bootstrap, all functions
(including those in modules enabled by the current page request) are
available when this hook is called. Use cases could be displaying a user
message, or calling a module function necessary for initial setup, etc.

Please be sure that anything added or modified in this function that can
be removed during uninstall should be removed with hook_uninstall().

@see hook_schema()
@see module_enable()
@see hook_enable()
@see hook_disable()
@see hook_uninstall()
@see hook_modules_installed()
```

## Code

```php
function hook_install() {
  // Populate the default {node_access} record.
  db_insert('node_access')
    ->fields(array(
      'nid' => 0,
      'gid' => 0,
      'realm' => 'all',
      'grant_view' => 1,
      'grant_update' => 0,
      'grant_delete' => 0,
    ))
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_install()".

- [actions_loop_test_install()](../../simpletest/tests/actions_loop_test.install/actions_loop_test_install.md) — `modules/simpletest/tests/actions_loop_test.install`
- [module_test_install()](../../simpletest/tests/module_test.install/module_test_install.md) — `modules/simpletest/tests/module_test.install`
- [block_install()](../../block/block.install/block_install.md) — `modules/block/block.install`
- [blog_install()](../../blog/blog.install/blog_install.md) — `modules/blog/blog.install`
- [book_install()](../../book/book.install/book_install.md) — `modules/book/book.install`
- [contact_install()](../../contact/contact.install/contact_install.md) — `modules/contact/contact.install`
- [field_test_install()](../../field/tests/field_test.install/field_test_install.md) — `modules/field/tests/field_test.install`
- [filter_install()](../../filter/filter.install/filter_install.md) — `modules/filter/filter.install`
- [forum_install()](../../forum/forum.install/forum_install.md) — `modules/forum/forum.install`
- [image_install()](../../image/image.install/image_install.md) — `modules/image/image.install`
- [locale_install()](../../locale/locale.install/locale_install.md) — `modules/locale/locale.install`
- [menu_install()](../../menu/menu.install/menu_install.md) — `modules/menu/menu.install`
- [minimal_install()](../../../profiles/minimal/minimal.install/minimal_install.md) — `profiles/minimal/minimal.install`
- [node_install()](../../node/node.install/node_install.md) — `modules/node/node.install`
- [openid_test_install()](../../openid/tests/openid_test.install/openid_test_install.md) — `modules/openid/tests/openid_test.install`
- [rdf_install()](../../rdf/rdf.install/rdf_install.md) — `modules/rdf/rdf.install`
- [rdf_test_install()](../../rdf/tests/rdf_test.install/rdf_test_install.md) — `modules/rdf/tests/rdf_test.install`
- [shortcut_install()](../../shortcut/shortcut.install/shortcut_install.md) — `modules/shortcut/shortcut.install`
- [standard_install()](../../../profiles/standard/standard.install/standard_install.md) — `profiles/standard/standard.install`
- [system_install()](../system.install/system_install.md) — `modules/system/system.install`
- [testing_install()](../../../profiles/testing/testing.install/testing_install.md) — `profiles/testing/testing.install`
- [trigger_install()](../../trigger/trigger.install/trigger_install.md) — `modules/trigger/trigger.install`
- [update_install()](../../update/update.install/update_install.md) — `modules/update/update.install`
- [user_install()](../../user/user.install/user_install.md) — `modules/user/user.install`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
