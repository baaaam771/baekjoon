fun main() {
    val inputDto = readInput()
    print(inputDto.findTotalFee())
}

data class InputDto(
    val teamCount: Int
) {
    private val feePerTeam = 4000

    fun findTotalFee(): Int {
        return teamCount * feePerTeam
    }
}

fun readInput(): InputDto {
    val teamCount = readLine()
        ?.toIntOrNull()
        ?: throw IllegalArgumentException("Invalid testCaseNum")
    
    return InputDto(teamCount)
}