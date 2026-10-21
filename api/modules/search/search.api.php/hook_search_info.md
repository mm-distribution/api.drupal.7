# hook_search_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/search/search.api.php`](_file.md), lines 42–51 · [local source](../../../../source/modules/search/search.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php#L42-L51)
- **Module/theme:** search
- **Topics:** [hooks](../../../topics/hooks.md), [search](../../../topics/search.md)

## Signature

```php
function hook_search_info()
```

## Documentation

```text
Define a custom search type.

This hook allows a module to tell search.module that it wishes to perform
searches on content it defines (custom node types, users, or comments for
example) when a site search is performed.

In order for the search to do anything, your module must also implement
hook_search_execute(), which is called when someone requests a search
on your module's type of content. If you want to have your content
indexed in the standard search index, your module should also implement
hook_update_index(). If your search type has settings, you can implement
hook_search_admin() to add them to the search settings page. You can use
hook_form_FORM_ID_alter(), with FORM_ID set to 'search_form', to add fields
to the search form (see node_form_search_form_alter() for an example).
You can use hook_search_access() to limit access to searching,
and hook_search_page() to override how search results are displayed.

@return
  Array with optional keys:
  - title: Title for the tab on the search page for this module. Title must
    be untranslated. Outside of this return array, pass the title through the
    t() function to register it as a translatable string.
  - path: Path component after 'search/' for searching with this module.
    Defaults to the module name if not given.
  - conditions_callback: An implementation of callback_search_conditions().

@ingroup search
```

## Code

```php
function hook_search_info() {
  // Make the title translatable.
  t('Content');

  return array(
    'title' => 'Content',
    'path' => 'node',
    'conditions_callback' => 'callback_search_conditions',
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_search_info()".

- [node_search_info()](../../node/node.module/node_search_info.md) — `modules/node/node.module`
- [search_extra_type_search_info()](../tests/search_extra_type.module/search_extra_type_search_info.md) — `modules/search/tests/search_extra_type.module`
- [user_search_info()](../../user/user.module/user_search_info.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/search/search.api.php](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
