# Behavior::assertCommand()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Behavior.php`](../_file.md), lines 93–105 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Behavior.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Behavior.php#L93-L105)
- **Class:** [Behavior](../Behavior.md)

## Signature

```php
private function assertCommand($command)
```

## Documentation

_No docblock in source._

## Code

```php
    private function assertCommand($command)
    {
        if (in_array($command, $this->availableCommands, true)) {
            return;
        }
        throw new \LogicException(
            sprintf(
                'Unknown command "%s"',
                $command
            ),
            1535189882
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Behavior.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Behavior.php) · Licensed GPL-2.0-or-later (see LICENSE)._
