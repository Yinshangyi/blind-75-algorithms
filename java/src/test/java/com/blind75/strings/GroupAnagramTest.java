package com.blind75.strings;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.List;

public class GroupAnagramTest {

    @Test
    public void testGroupAnagram1() {
        var inputStrings = List.of("eat", "tea", "tan", "ate", "nat", "bat");
        var groups = new GroupAnagram().groupAnagrams(inputStrings);
        var expectedGroups = List.of(
                List.of("tan", "nat"),
                List.of("bat"),
                List.of("eat", "tea", "ate")
        );
        Assertions.assertEquals(expectedGroups, groups);
    }

    @Test
    public void testGroupAnagram2() {
        var inputStrings = List.of("");
        var groups = new GroupAnagram().groupAnagrams(inputStrings);
        Assertions.assertEquals(1, groups.size());
        Assertions.assertEquals("", groups.get(0).get(0));
    }

    @Test
    public void testGroupAnagram3() {
        var inputStrings = List.of("a");
        var groups = new GroupAnagram().groupAnagrams(inputStrings);
        var expectedGroups = List.of(List.of("a"));
        Assertions.assertEquals(groups, expectedGroups);
    }
}
