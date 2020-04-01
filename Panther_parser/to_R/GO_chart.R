#################################
# Plot gene ontology enrichment #
#################################

# Requires the package 'ggplot2' (needs to be installed first)
# Load the ggplot2 package
library(ggplot2)
library(plotscale)

# set the working directory where the tables to use are located
args <- commandArgs(trailingOnly=TRUE)

#get the file name and path from terminal 
wd<-getwd()
slash<-'/'
#the paste function join together the working directory (wd) a slash(variable created above) and the csv file name given in terminal
path_file <- paste(wd,slash,args[1],sep= "",collapse=NULL)

#############################################
# PART 1: plot the representative enriched
# GO terms in the list of all DEGs (Figure 2)
#############################################

# Prepare dataframe
#------------------
# Import the table containing the enriched GO terms and output file name
GO_all <- read.csv(path_file,header=T,stringsAsFactors = T)
input_file_name <- tools::file_path_sans_ext(basename(path_file))
output_file_name <- paste(input_file_name, ".pdf",sep= "",collapse=NULL)
# List objects and their structure contained in the dataframe 'GO_all'
ls.str(GO_all)

# Transform the column 'Gene_number' into a numeric variable
GO_all$Gene_number <- as.numeric(GO_all$Gene_number)

# Replace all the "_" by a space in the column containing the GO terms
GO_all$GO <- chartr("_", " ", GO_all$GO)

# Transform FDR values by -log10('FDR values')
GO_all$'|log10(FDR)|' <- -(log10(GO_all$FDR))

# Draw the plot with ggplot2 (Figure 2)
#--------------------------------------

fig1 <- ggplot(GO_all, aes(x = GO, y = Fold_enrichment)) +
  geom_hline(yintercept = 1, linetype="dashed", 
             color = "azure4", size=.5)+
  geom_point(data=GO_all,aes(x=GO, y=Fold_enrichment,size = Gene_number, colour = `|log10(FDR)|`), alpha=.7)+
  scale_x_discrete(limits= GO_all$GO)+
  scale_color_gradient(low="green",high="red",limits=c(0, NA))+
  coord_flip()+
  theme_bw()+
  theme(axis.ticks.length=unit(-0.1, "cm"),
        axis.text.x = element_text(margin=margin(5,5,0,5,"pt")),
        axis.text.y = element_text(margin=margin(5,5,5,5,"pt")),
        axis.text = element_text(color = "black"),
        panel.grid.minor = element_blank(),
        legend.title.align=0.5)+
  xlab("GO")+
  ylab("Fold enrichment")+
  labs(color="-log10(FDR)", size="Number\nof genes")+ #Replace by your variable names; \n allow a new line for text
  guides(y = guide_axis(order=2), colour = guide_colourbar(order=1))

pdf(output_file_name)
fig1
dev.off()

#plotsize(fig1,width = 3, height = 20)

#ds <- devsize(fig1, width = 1, height = 15)
#as.png(fig1, filename = output_file_name, width = ds$width, height = ds$height)


