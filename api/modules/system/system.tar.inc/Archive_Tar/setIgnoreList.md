# Archive_Tar::setIgnoreList()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 793–798 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L793-L798)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function setIgnoreList($list)
```

## Documentation

```text
This method sets the regular expression for ignoring all files and directories
matching the filenames in the array list at import, for example:
$arch->setIgnoreList(array('CVS', '.svn', 'bin/tool'));

@param array $list a list of file or directory names to ignore

@access public
```

## Code

```php
    public function setIgnoreList($list)
    {
        $list = str_replace(array('#', '.', '^', '$'), array('\#', '\.', '\^', '\$'), $list);
        $regexp = '#/' . join('$|/', $list) . '#';
        $this->setIgnoreRegexp($regexp);
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
