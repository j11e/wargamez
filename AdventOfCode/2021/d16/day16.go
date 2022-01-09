package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Packet struct {
	version    int64
	typeId     string
	subPackets []*Packet
	value      int64
}

func (p *Packet) toString(depth int) {
	indent := ""
	for i := 0; i < depth; i++ {
		indent += "  "
	}

	fmt.Print(indent, "Packet with version = ", p.version, ", typeId = ", p.typeId)

	if len(p.subPackets) > 0 {
		fmt.Println(", and subpackets: ")
		for j := 0; j < len(p.subPackets); j++ {
			p.subPackets[j].toString(depth + 1)
		}
	} else {
		fmt.Println(" and literal value ", p.value)
	}
}

func (p *Packet) recursiveSumVersions() int {
	sum := p.version

	if len(p.subPackets) > 0 {
		for j := 0; j < len(p.subPackets); j++ {
			sum += int64(p.subPackets[j].recursiveSumVersions())
		}
	}

	return int(sum)
}

func main() {
	b, err := os.ReadFile("./day16_test.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(b), "\n")

	hex := lines[0]

	hexmap := map[byte]string{
		'0': "0000",
		'1': "0001",
		'2': "0010",
		'3': "0011",
		'4': "0100",
		'5': "0101",
		'6': "0110",
		'7': "0111",
		'8': "1000",
		'9': "1001",
		'A': "1010",
		'B': "1011",
		'C': "1100",
		'D': "1101",
		'E': "1110",
		'F': "1111",
	}

	binstr := ""
	for i := 0; i < len(hex); i++ {
		binstr += hexmap[hex[i]]
	}

	root, _ := nextPacket(binstr, 0)

	root.toString(0)
	fmt.Println("p1 sum: ", root.recursiveSumVersions())
}

func nextPacket(binstr string, cursor int) (*Packet, int) {
	var p *Packet
	v := binstr[cursor : cursor+3]
	version, _ := strconv.ParseInt(v, 2, 64)
	cursor += 3

	typeId := binstr[cursor : cursor+3]
	cursor += 3

	p = &Packet{version, typeId, []*Packet{}, 0}

	switch typeId {
	case "100":
		p, cursor = handleLiteralValue(binstr, cursor, p)
	default:
		p, cursor = handleOperator(binstr, cursor, p)
	}

	return p, cursor
}

func handleLiteralValue(binstr string, cursor int, p *Packet) (*Packet, int) {
	leadingBit := '1'
	payload := ""

	for leadingBit == '1' {
		g := binstr[cursor : cursor+5]
		cursor += 5
		leadingBit = rune(g[0])
		payload += g[1:]
	}

	i, _ := strconv.ParseInt(payload, 2, 64)

	(*p).value = i

	return p, cursor
}

func handleOperator(binstr string, cursor int, p *Packet) (*Packet, int) {
	mode := binstr[cursor]
	cursor += 1

	var packs []*Packet
	switch mode {
	case '0':
		// next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet
		length, _ := strconv.ParseInt(binstr[cursor:cursor+15], 2, 64)
		cursor += 15
		subbinstr := binstr[cursor : cursor+int(length)]
		subcursor := 0
		packs = make([]*Packet, 0)
		for subcursor < int(length) {
			p, s := nextPacket(subbinstr, subcursor)
			subcursor = s
			packs = append(packs, p)
		}

	case '1':
		// next 11 bits are a number that represents the number of sub-packets immediately contained by this packet
		length, _ := strconv.ParseInt(binstr[cursor:cursor+11], 2, 64)
		cursor += 11
		packs = make([]*Packet, length)
		for i := 0; i < int(length); i++ {
			p, s := nextPacket(binstr, cursor)
			cursor = s
			packs[i] = p
		}
	}

	p.subPackets = packs

	return p, cursor
}
