# Behavior::assertAssertionCompleteness()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Behavior.php`](../_file.md), lines 107–123 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Behavior.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Behavior.php#L107-L123)
- **Class:** [Behavior](../Behavior.md)

## Signature

```php
private function assertAssertionCompleteness()
```

## Documentation

_No docblock in source._

## Code

```php
    private function assertAssertionCompleteness()
    {
        $undefinedAssertions = array_diff(
            $this->availableCommands,
            array_keys($this->assertions)
        );
        if (empty($undefinedAssertions)) {
            return;
        }
        throw new \LogicException(
            sprintf(
                'Missing assertions for commands: %s',
                implode(', ', $undefinedAssertions)
            ),
            1535189883
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Behavior.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Behavior.php) · Licensed GPL-2.0-or-later (see LICENSE)._
