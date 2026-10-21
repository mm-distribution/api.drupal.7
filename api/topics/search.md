# Search interface

- **Topic id:** `search`
- **Defined in:** [`modules/search/search.module`](../modules/search/search.module/_file.md), line 911 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L911)

## Documentation

```text
@defgroup search Search interface
@{
The Drupal search interface manages a global search mechanism.

Modules may plug into this system to provide searches of different types of
data. Most of the system is handled by search.module, so this must be enabled
for all of the search features to work.

There are three ways to interact with the search system:
- Specifically for searching nodes, you can implement
  hook_node_update_index() and hook_node_search_result(). However, note that
  the search system already indexes all visible output of a node; i.e.,
  everything displayed normally by hook_view() and hook_node_view(). This is
  usually sufficient. You should only use this mechanism if you want
  additional, non-visible data to be indexed.
- Implement hook_search_info(). This will create a search tab for your module
  on the /search page with a simple keyword search form. You will also need
  to implement hook_search_execute() to perform the search.
- Implement hook_update_index(). This allows your module to use Drupal's
  HTML indexing mechanism for searching full text efficiently.

If your module needs to provide a more complicated search form, then you need
to implement it yourself without hook_search_info(). In that case, you should
define it as a local task (tab) under the /search page (e.g. /search/mymodule)
so that users can easily find it.
```

## Members (derived, 16)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [callback_search_conditions()](../modules/search/search.api.php/callback_search_conditions.md) (function) — Provide search query conditions.
- [hook_search_access()](../modules/search/search.api.php/hook_search_access.md) (function) — Define access to a custom search routine.
- [hook_search_admin()](../modules/search/search.api.php/hook_search_admin.md) (function) — Add elements to the search settings form.
- [hook_search_execute()](../modules/search/search.api.php/hook_search_execute.md) (function) — Execute a search for a set of key words.
- [hook_search_info()](../modules/search/search.api.php/hook_search_info.md) (function) — Define a custom search type.
- [hook_search_preprocess()](../modules/search/search.api.php/hook_search_preprocess.md) (function) — Preprocess text for search.
- [hook_search_reset()](../modules/search/search.api.php/hook_search_reset.md) (function) — Take action when the search index is going to be rebuilt.
- [hook_search_status()](../modules/search/search.api.php/hook_search_status.md) (function) — Report the status of indexing.
- [hook_update_index()](../modules/search/search.api.php/hook_update_index.md) (function) — Update the search index for this module.
- [search_box()](../modules/search/search.module/search_box.md) (function) — Form builder; Output a search form for the search block's search box.
- [search_box_form_submit()](../modules/search/search.module/search_box_form_submit.md) (function) — Process a block search form submission.
- [search_data()](../modules/search/search.module/search_data.md) (function) — Performs a search by calling hook_search_execute().
- [search_excerpt()](../modules/search/search.module/search_excerpt.md) (function) — Returns snippets from a piece of text, with certain keywords highlighted. Used for formatting search results.
- [search_form()](../modules/search/search.module/search_form.md) (function) — Builds a search form.
- [search_index()](../modules/search/search.module/search_index.md) (function) — Update the full-text search index for a particular item.
- [template_preprocess_search_block_form()](../modules/search/search.module/template_preprocess_search_block_form.md) (function) — Process variables for search-block-form.tpl.php.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
