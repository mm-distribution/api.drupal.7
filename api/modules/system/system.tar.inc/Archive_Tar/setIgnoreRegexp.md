# Archive_Tar::setIgnoreRegexp()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 779–782 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L779-L782)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function setIgnoreRegexp($regexp)
```

## Documentation

```text
This method sets the regular expression for ignoring files and directories
at import, for example:
$arch->setIgnoreRegexp("#CVS|\.svn#");

@param string $regexp regular expression defining which files or directories to ignore
```

## Code

```php
    public function setIgnoreRegexp($regexp)
    {
        $this->_ignore_regexp = $regexp;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
