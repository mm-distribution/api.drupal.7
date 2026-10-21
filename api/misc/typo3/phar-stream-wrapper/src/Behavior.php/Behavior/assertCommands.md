# Behavior::assertCommands()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Behavior.php`](../_file.md), lines 78–91 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Behavior.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Behavior.php#L78-L91)
- **Class:** [Behavior](../Behavior.md)

## Signature

```php
private function assertCommands(array $commands)
```

## Documentation

```text
@param array $commands
```

## Code

```php
    private function assertCommands(array $commands)
    {
        $unknownCommands = array_diff($commands, $this->availableCommands);
        if (empty($unknownCommands)) {
            return;
        }
        throw new \LogicException(
            sprintf(
                'Unknown commands: %s',
                implode(', ', $unknownCommands)
            ),
            1535189881
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Behavior.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Behavior.php) · Licensed GPL-2.0-or-later (see LICENSE)._
