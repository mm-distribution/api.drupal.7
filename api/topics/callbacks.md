# Callbacks

- **Topic id:** `callbacks`
- **Defined in:** [`includes/module.inc`](../includes/module.inc/_file.md), line 646 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L646)

## Documentation

```text
@defgroup callbacks Callbacks
@{
Callback function signatures.

Drupal's API sometimes uses callback functions to allow you to define how
some type of processing happens. A callback is a function with a defined
signature, which you define in a module. Then you pass the function name as
a parameter to a Drupal API function or return it as part of a hook
implementation return value, and your function is called at an appropriate
time. For instance, when setting up batch processing you might need to
provide a callback function for each processing step and/or a callback for
when processing is finished; you would do that by defining these functions
and passing their names into the batch setup function.

Callback function signatures, like hook definitions, are described by
creating and documenting dummy functions in a *.api.php file; normally, the
dummy callback function's name should start with "callback_", and you should
document the parameters and return value and provide a sample function body.
Then your API documentation can refer to this callback function in its
documentation. A user of your API can usually name their callback function
anything they want, although a standard name would be to replace "callback_"
with the module name.

@see hooks
@see themeable

@}
```

## Members (derived, 11)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [callback_batch_finished()](../modules/system/form.api.php/callback_batch_finished.md) (function) — Complete a batch process.
- [callback_batch_operation()](../modules/system/form.api.php/callback_batch_operation.md) (function) — Perform a single batch operation.
- [callback_entity_info_label()](../modules/system/system.api.php/callback_entity_info_label.md) (function) — Return the label of an entity.
- [callback_entity_info_language()](../modules/system/system.api.php/callback_entity_info_language.md) (function) — Return the language code of the entity.
- [callback_entity_info_uri()](../modules/system/system.api.php/callback_entity_info_uri.md) (function) — Return the URI for an entity.
- [callback_filter_prepare()](../modules/filter/filter.api.php/callback_filter_prepare.md) (function) — Provide prepared text with special characters escaped.
- [callback_filter_process()](../modules/filter/filter.api.php/callback_filter_process.md) (function) — Provide text filtered to conform to the supplied format.
- [callback_filter_settings()](../modules/filter/filter.api.php/callback_filter_settings.md) (function) — Provide a settings form for filter settings.
- [callback_filter_tips()](../modules/filter/filter.api.php/callback_filter_tips.md) (function) — Return help text for a filter.
- [callback_queue_worker()](../modules/system/system.api.php/callback_queue_worker.md) (function) — Work on a single queue item.
- [callback_search_conditions()](../modules/search/search.api.php/callback_search_conditions.md) (function) — Provide search query conditions.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
