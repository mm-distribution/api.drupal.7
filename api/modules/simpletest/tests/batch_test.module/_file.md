# modules/simpletest/tests/batch_test.module

- **Source:** [local](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · 514 lines
- **Module/theme:** batch_test

## File documentation

```text
@file
Helper module for the Batch API tests.
```

## Functions (derived index)

- [batch_test_menu()](batch_test_menu.md) — Implement hook_menu().
- [batch_test_simple_form()](batch_test_simple_form.md) — Simple form.
- [batch_test_simple_form_submit()](batch_test_simple_form_submit.md) — Submit handler for the simple form.
- [batch_test_multistep_form()](batch_test_multistep_form.md) — Multistep form.
- [batch_test_multistep_form_submit()](batch_test_multistep_form_submit.md) — Submit handler for the multistep form.
- [batch_test_chained_form()](batch_test_chained_form.md) — Form with chained submit callbacks.
- [batch_test_chained_form_submit_1()](batch_test_chained_form_submit_1.md) — Submit handler #1 for the chained form.
- [batch_test_chained_form_submit_2()](batch_test_chained_form_submit_2.md) — Submit handler #2 for the chained form.
- [batch_test_chained_form_submit_3()](batch_test_chained_form_submit_3.md) — Submit handler #3 for the chained form.
- [batch_test_chained_form_submit_4()](batch_test_chained_form_submit_4.md) — Submit handler #4 for the chained form.
- [batch_test_programmatic()](batch_test_programmatic.md) — Menu callback: programmatically submits the 'Chained' form.
- [batch_test_nested_drupal_form_submit()](batch_test_nested_drupal_form_submit.md) — Menu callback: programmatically submits a form within a batch.
- [_batch_test_nested_drupal_form_submit_callback()](_batch_test_nested_drupal_form_submit_callback.md) — Batch operation: submits form_test_mock_form using drupal_form_submit().
- [batch_test_mock_form()](batch_test_mock_form.md) — A simple form with a textfield and submit button.
- [batch_test_mock_form_submit()](batch_test_mock_form_submit.md) — Submit handler for the batch_test_mock form.
- [batch_test_no_form()](batch_test_no_form.md) — Menu callback: fire a batch process without a form submission.
- [batch_test_large_percentage()](batch_test_large_percentage.md) — Menu callback: fire a batch process without a form submission.
- [batch_test_redirect_page()](batch_test_redirect_page.md) — Menu callback: successful redirection.
- [_batch_test_batch_0()](_batch_test_batch_0.md) — Batch 0: no operation.
- [_batch_test_batch_1()](_batch_test_batch_1.md) — Batch 1: repeats a simple operation.
- [_batch_test_batch_2()](_batch_test_batch_2.md) — Batch 2: single multistep operation.
- [_batch_test_batch_3()](_batch_test_batch_3.md) — Batch 3: both single and multistep operations.
- [_batch_test_batch_4()](_batch_test_batch_4.md) — Batch 4: batch within a batch.
- [_batch_test_batch_5()](_batch_test_batch_5.md) — Batch 5: repeats a simple operation.
- [batch_test_theme_batch()](batch_test_theme_batch.md) — Menu callback: run a batch for testing theme used on the progress page.
- [_batch_test_theme_callback()](_batch_test_theme_callback.md) — Batch callback function for testing the theme used on the progress page.
- [batch_test_stack()](batch_test_stack.md) — Helper function: store or retrieve traced execution data.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
