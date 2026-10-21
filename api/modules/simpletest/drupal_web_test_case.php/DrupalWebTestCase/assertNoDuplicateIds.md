# DrupalWebTestCase::assertNoDuplicateIds()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3903–3914 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3903-L3914)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertNoDuplicateIds($message = '', $group = 'Other', $ids_to_skip = array())
```

## Documentation

```text
Asserts that each HTML ID is used for just a single element.

@param $message
  Message to display.
@param $group
  The group this message belongs to.
@param $ids_to_skip
  An optional array of ids to skip when checking for duplicates. It is
  always a bug to have duplicate HTML IDs, so this parameter is to enable
  incremental fixing of core code. Whenever a test passes this parameter,
  it should add a "todo" comment above the call to this function explaining
  the legacy bug that the test wishes to ignore and including a link to an
  issue that is working to fix that legacy bug.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertNoDuplicateIds($message = '', $group = 'Other', $ids_to_skip = array()) {
    $status = TRUE;
    foreach ($this->xpath('//*[@id]') as $element) {
      $id = (string) $element['id'];
      if (isset($seen_ids[$id]) && !in_array($id, $ids_to_skip)) {
        $this->fail(t('The HTML ID %id is unique.', array('%id' => $id)), $group);
        $status = FALSE;
      }
      $seen_ids[$id] = TRUE;
    }
    return $this->assert($status, $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
