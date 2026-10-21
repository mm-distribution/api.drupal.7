# SimpleTestFunctionalTest::getTestResults()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 283–307 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L283-L307)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
- **Module/theme:** simpletest

## Signature

```php
function getTestResults()
```

## Documentation

```text
Get the results from a test and store them in the class array $results.
```

## Code

```php
  function getTestResults() {
    $results = array();
    if ($this->parse()) {
      if ($fieldset = $this->getResultFieldSet()) {
        // Code assumes this is the only test in group.
        $results['summary'] = $this->asText($fieldset->div->div[1]);
        $results['name'] = $this->asText($fieldset->legend);

        $results['assertions'] = array();
        $tbody = $fieldset->div->table->tbody;
        foreach ($tbody->tr as $row) {
          $assertion = array();
          $assertion['message'] = $this->asText($row->td[0]);
          $assertion['type'] = $this->asText($row->td[1]);
          $assertion['file'] = $this->asText($row->td[2]);
          $assertion['line'] = $this->asText($row->td[3]);
          $assertion['function'] = $this->asText($row->td[4]);
          $ok_url = file_create_url('misc/watchdog-ok.png');
          $assertion['status'] = ($row->td[5]->img['src'] == $ok_url) ? 'Pass' : 'Fail';
          $results['assertions'][] = $assertion;
        }
      }
    }
    $this->childTestResults = $results;
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
