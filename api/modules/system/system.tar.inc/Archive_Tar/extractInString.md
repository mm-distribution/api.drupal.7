# Archive_Tar::extractInString()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 656–666 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L656-L666)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function extractInString($p_filename)
```

## Documentation

```text
This method extract from the archive one file identified by $p_filename.
The return value is a string with the file content, or NULL on error.

@param string $p_filename The path of the file to extract in a string.

@return a string with the file content or NULL.
```

## Code

```php
    public function extractInString($p_filename)
    {
        if ($this->_openRead()) {
            $v_result = $this->_extractInString($p_filename);
            $this->_close();
        } else {
            $v_result = null;
        }

        return $v_result;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
