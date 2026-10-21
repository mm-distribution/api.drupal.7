# BatchProcessingTestCase::_resultMessages()

- **Type:** Method
- **File:** [`modules/simpletest/tests/batch.test`](../_file.md), lines 238–274 · [local source](../../../../../../source/modules/simpletest/tests/batch.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test#L238-L274)
- **Class:** [BatchProcessingTestCase](../BatchProcessingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function _resultMessages($id)
```

## Documentation

```text
Helper function: return expected result messages for the test batches.
```

## Code

```php
  function _resultMessages($id) {
    $messages = array();

    switch ($id) {
      case 'batch_0':
        $messages[] = 'results for batch 0<br />none';
        break;

      case 'batch_1':
        $messages[] = 'results for batch 1<br />op 1: processed 10 elements';
        break;

      case 'batch_2':
        $messages[] = 'results for batch 2<br />op 2: processed 10 elements';
        break;

      case 'batch_3':
        $messages[] = 'results for batch 3<br />op 1: processed 10 elements<br />op 2: processed 10 elements';
        break;

      case 'batch_4':
        $messages[] = 'results for batch 4<br />op 1: processed 10 elements';
        $messages = array_merge($messages, $this->_resultMessages('batch_2'));
        break;

      case 'batch_5':
        $messages[] = 'results for batch 5<br />op 1: processed 10 elements. $context[\'finished\'] > 1 returned from batch process, with success.';
        break;

      case 'chained':
        $messages = array_merge($messages, $this->_resultMessages('batch_1'));
        $messages = array_merge($messages, $this->_resultMessages('batch_2'));
        $messages = array_merge($messages, $this->_resultMessages('batch_3'));
        break;
    }
    return $messages;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test) · Licensed GPL-2.0-or-later (see LICENSE)._
