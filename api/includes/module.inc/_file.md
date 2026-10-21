# includes/module.inc

- **Source:** [local](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · 1175 lines

## File documentation

```text
@file
API for loading and interacting with Drupal modules.
```

## Functions (derived index)

- [module_load_all()](module_load_all.md) — Loads all the modules that have been enabled in the system table.
- [module_list()](module_list.md) — Returns a list of currently active modules.
- [system_list()](system_list.md) — Builds a list of bootstrap modules and enabled modules and themes.
- [system_list_reset()](system_list_reset.md) — Resets all system_list() caches.
- [_module_build_dependencies()](_module_build_dependencies.md) — Determines which modules require and are required by each module.
- [module_exists()](module_exists.md) — Determines whether a given module exists.
- [module_load_install()](module_load_install.md) — Loads a module's installation hooks.
- [module_load_include()](module_load_include.md) — Loads a module include file.
- [module_load_all_includes()](module_load_all_includes.md) — Loads an include file for each module enabled in the {system} table.
- [module_enable()](module_enable.md) — Enables or installs a given list of modules.
- [module_disable()](module_disable.md) — Disables a given set of modules.
- [module_hook()](module_hook.md) — Determines whether a module implements a hook.
- [module_implements()](module_implements.md) — Determines which modules are implementing a hook.
- [module_hook_info()](module_hook_info.md) — Retrieves a list of hooks that are declared through hook_hook_info().
- [module_implements_write_cache()](module_implements_write_cache.md) — Writes the hook implementation cache.
- [module_invoke()](module_invoke.md) — Invokes a hook in a particular module.
- [module_invoke_all()](module_invoke_all.md) — Invokes a hook in all enabled modules that implement it.
- [drupal_required_modules()](drupal_required_modules.md) — Returns an array of modules required by core.
- [drupal_alter()](drupal_alter.md) — Passes alterable variables to specific hook_TYPE_alter() implementations.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
