# FormsTriggeringElementTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/form.test`](_file.md), lines 2005–2098 · [local source](../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L2005-L2098)
- **Module/theme:** batch_test

## Signature

```php
class FormsTriggeringElementTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test that FAPI correctly determines $form_state['triggering_element'].
```

## Methods (derived index)

- [getInfo()](FormsTriggeringElementTestCase/getInfo.md)
- [setUp()](FormsTriggeringElementTestCase/setUp.md)
- [testNoButtonInfoInPost()](FormsTriggeringElementTestCase/testNoButtonInfoInPost.md) — Test the determination of $form_state['triggering_element'] when no button information is included in the POST data, as is sometimes the case when the ENTER key is pressed in a textfield in Internet Explorer.
- [testAttemptAccessControlBypass()](FormsTriggeringElementTestCase/testAttemptAccessControlBypass.md) — Test that $form_state['triggering_element'] does not get set to a button with #access=FALSE.

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
